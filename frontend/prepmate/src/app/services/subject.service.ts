import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class SubjectService {
  private baseUrl = environment.apiUrl + '/subjects';
  private selectionUrl = environment.apiUrl + '/profile/subjects';

  constructor(private http: HttpClient) {}

  getSubjects(): Observable<any[]> {
    return this.http.get<any[]>(this.baseUrl);
  }

  saveSelectedSubjects(names: string[]) {
    localStorage.setItem('selectedSubjects', JSON.stringify(names));
    this.updateSelectedSubjects(names).subscribe();
  }

  getSelectedSubjects(): string[] {
    const data = localStorage.getItem('selectedSubjects');
    return data ? JSON.parse(data) : [];
  }

  updateSelectedSubjects(names: string[]) {
    return this.http.put<{ selected_subjects: string[] }>(this.selectionUrl, { subjects: names });
  }

  fetchSelectedSubjects() {
    return this.http.get<{ selected_subjects: string[] }>(this.selectionUrl);
  }
}
