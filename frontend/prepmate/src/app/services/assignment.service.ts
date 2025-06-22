import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class AssignmentService {
  private baseUrl = environment.apiUrl + '/api/assignments';

  constructor(private http: HttpClient) {}

  submitAssignment(payload: {
    user_id: number;
    exercise_id: number;
    respuesta_entregada: string;
    correcta: boolean;
  }) {
    return this.http.post(this.baseUrl, payload);
  }
}
