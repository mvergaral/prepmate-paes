import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

export interface SubjectProgress {
  subject: string;
  total: number;
  correct: number;
}

@Injectable({ providedIn: 'root' })
export class ProgressService {
  private baseUrl = environment.apiUrl + '/api/progress';

  constructor(private http: HttpClient) {}

  getProgress(userId: number): Observable<{ progress: SubjectProgress[] }> {
    return this.http.get<{ progress: SubjectProgress[] }>(`${this.baseUrl}/${userId}`);
  }
}
