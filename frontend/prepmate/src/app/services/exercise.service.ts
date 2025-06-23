import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

export interface Exercise {
  id: number;
  title: string;
  description: string;
  options: Record<string, string>;
  correct_answer: string;
  subject_id: number;
}

@Injectable({ providedIn: 'root' })
export class ExerciseService {
  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) {}

  getExercisesByMateria(materia: string, difficulty?: string): Observable<Exercise[]> {
    const params = [`materia=${materia}`];
    if (difficulty) {
      params.push(`difficulty=${difficulty}`);
    }
    return this.http.get<Exercise[]>(`${this.baseUrl}/api/exercises?${params.join('&')}`);
  }
}
