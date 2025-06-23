import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ExerciseService, Exercise } from '../../services/exercise.service';
import { AssignmentService } from '../../services/assignment.service';
import { AuthStore } from '../../store/auth.store';
import { ToastController } from '@ionic/angular';

@Component({
  selector: 'app-session',
  templateUrl: './session.page.html',
  styleUrls: ['./session.page.scss'],
  standalone: false,
})
export class SessionPage implements OnInit {
  materia = '';
  exercises: Exercise[] = [];
  index = 0;
  selected: string | null = null;
  correct = 0;
  asked = 0;
  totalExercises = 0;
  answeredIds = new Set<number>();
  streakCorrect = 0;
  streakWrong = 0;
  loading = false;
  difficultyLevels = ['fácil', 'media', 'difícil'];
  difficultyIndex = 0;

  constructor(
    private route: ActivatedRoute,
    private exerciseService: ExerciseService,
    private assignmentService: AssignmentService,
    private store: AuthStore,
    private toastCtrl: ToastController
  ) {}

  async showResult(correct: boolean) {
    const toast = await this.toastCtrl.create({
      message: correct ? '¡Respuesta correcta!' : 'Respuesta incorrecta.',
      duration: 1500,
      color: correct ? 'success' : 'danger',
      position: 'top'
    });
    await toast.present();
  }

  ngOnInit() {
    this.materia = this.route.snapshot.paramMap.get('materia') || '';
    this.exerciseService
      .getExercisesByMateria(this.materia)
      .subscribe((res) => (this.totalExercises = res.length));
    this.loadExercises();
  }

  get difficulty() {
    return this.difficultyLevels[this.difficultyIndex];
  }

  loadExercises() {
    this.exerciseService
      .getExercisesByMateria(this.materia, this.difficulty)
      .subscribe((res) => {
        // filtrar ejercicios ya respondidos
        this.exercises = res.filter((e) => !this.answeredIds.has(e.id));
        this.index = 0;
        if (this.exercises.length === 0) {
          // si no quedan ejercicios pendientes, finalizar la sesión
          this.asked = this.maxQuestions;
        } else {
          this.loadCurrent();
        }
      });
  }

  get current() {
    return this.exercises[this.index];
  }

  get done() {
    return this.asked >= this.maxQuestions;
  }

  get answeredCount() {
    return this.answeredIds.size;
  }

  get maxQuestions() {
    return Math.min(10, this.totalExercises);
  }

  loadCurrent() {
    this.selected = null;
    this.loading = false;
  }

  submit() {
    if (!this.current || !this.selected || this.loading) {
      return;
    }
    const user = this.store['state'].user;
    const current = this.current;
    const answer = this.selected;
    const isCorrect = answer === current.correct_answer;
    this.loading = true;
    this.assignmentService
      .submitAssignment({
        user_id: user.id,
        exercise_id: current.id,
        respuesta_entregada: answer,
        correcta: isCorrect,
      })
      .subscribe(() => {
        this.loading = false;
        this.afterSubmit(isCorrect, current.id);
      });
  }

  private afterSubmit(isCorrect: boolean, id: number) {
    this.showResult(isCorrect);
    if (isCorrect) {
      this.correct++;
      this.streakCorrect++;
      this.streakWrong = 0;
    } else {
      this.streakWrong++;
      this.streakCorrect = 0;
    }

    if (!this.answeredIds.has(id)) {
      this.answeredIds.add(id);
      this.asked++;
    }

    if (this.streakCorrect >= 2 && this.difficultyIndex < this.difficultyLevels.length - 1) {
      this.difficultyIndex++;
      this.streakCorrect = 0;
      this.loadExercises();
      return;
    }
    if (this.streakWrong >= 2 && this.difficultyIndex > 0) {
      this.difficultyIndex--;
      this.streakWrong = 0;
      this.loadExercises();
      return;
    }

    this.index++;
    if (this.index >= this.exercises.length) {
      this.loadExercises();
    } else {
      this.loadCurrent();
    }
  }

  restart() {
    this.correct = 0;
    this.asked = 0;
    this.answeredIds.clear();
    this.streakCorrect = 0;
    this.streakWrong = 0;
    this.loading = false;
    this.difficultyIndex = 0;
    this.exerciseService
      .getExercisesByMateria(this.materia)
      .subscribe((res) => (this.totalExercises = res.length));
    this.loadExercises();
  }
}
