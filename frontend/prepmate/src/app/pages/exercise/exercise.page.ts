import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ExerciseService, Exercise } from '../../services/exercise.service';
import { AssignmentService } from '../../services/assignment.service';
import { AuthStore } from '../../store/auth.store';

@Component({
  selector: 'app-exercise',
  templateUrl: './exercise.page.html',
  styleUrls: ['./exercise.page.scss'],
  standalone: false
})
export class ExercisePage implements OnInit {
  materia = '';
  exercises: Exercise[] = [];
  selected: Record<number, string> = {};

  constructor(
    private route: ActivatedRoute,
    private exerciseService: ExerciseService,
    private assignmentService: AssignmentService,
    private store: AuthStore
  ) {}

  ngOnInit() {
    this.materia = this.route.snapshot.paramMap.get('materia') || '';
    this.exerciseService.getExercisesByMateria(this.materia).subscribe(res => (this.exercises = res));
  }

  submit(ex: Exercise) {
    const answer = this.selected[ex.id];
    if (!answer) { return; }
    const user = this.store['state'].user; // simple access
    this.assignmentService.submitAssignment({
      user_id: user.id,
      exercise_id: ex.id,
      respuesta_entregada: answer,
      correcta: answer === ex.correct_answer
    }).subscribe();
  }
}
