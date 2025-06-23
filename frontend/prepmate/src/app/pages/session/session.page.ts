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

  constructor(
    private route: ActivatedRoute,
    private exerciseService: ExerciseService,
    private assignmentService: AssignmentService,
    private store: AuthStore
  ) {}

  ngOnInit() {
    this.materia = this.route.snapshot.paramMap.get('materia') || '';
    this.exerciseService.getExercisesByMateria(this.materia).subscribe((res) => {
      this.exercises = res;
      this.loadCurrent();
    });
  }

  get current() {
    return this.exercises[this.index];
  }

  get done() {
    return this.index >= this.exercises.length;
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
    }
    this.index++;
    this.loadCurrent();
  }
}
