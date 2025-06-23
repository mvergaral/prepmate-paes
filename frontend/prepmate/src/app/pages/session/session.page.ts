import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ExerciseService, Exercise } from '../../services/exercise.service';
import { AssignmentService } from '../../services/assignment.service';
import { AuthStore } from '../../store/auth.store';

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
  streakCorrect = 0;
  streakWrong = 0;
  difficultyLevels = ['fácil', 'media', 'difícil'];
  difficultyIndex = 0;

  constructor(
    private route: ActivatedRoute,
    private exerciseService: ExerciseService,
    private assignmentService: AssignmentService,
    private store: AuthStore
  ) {}

  ngOnInit() {
    this.materia = this.route.snapshot.paramMap.get('materia') || '';
    this.loadExercises();
  }

  get difficulty() {
    return this.difficultyLevels[this.difficultyIndex];
  }

  loadExercises() {
    this.exerciseService
      .getExercisesByMateria(this.materia, this.difficulty)
      .subscribe((res) => {
        this.exercises = res;
        this.index = 0;
        this.loadCurrent();
      });
  }

  get current() {
    return this.exercises[this.index];
  }

  get done() {
    return this.asked >= this.maxQuestions;
  }

  get maxQuestions() {
    return 10;
  }

  loadCurrent() {
    this.selected = null;
  }

  submit() {
    if (!this.current || !this.selected) {
      return;
    }
    const user = this.store['state'].user;
    const isCorrect = this.selected === this.current.correct_answer;
    this.assignmentService
      .submitAssignment({
        user_id: user.id,
        exercise_id: this.current.id,
        respuesta_entregada: this.selected,
        correcta: isCorrect,
      })
      .subscribe();
    if (isCorrect) {
      this.correct++;
      this.streakCorrect++;
      this.streakWrong = 0;
    } else {
      this.streakWrong++;
      this.streakCorrect = 0;
    }
    this.asked++;

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
}
