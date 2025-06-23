import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class NotificationService {
  private baseUrl = environment.apiUrl + '/api/notifications';
  private messageSubject = new BehaviorSubject<string | null>(null);
  message$ = this.messageSubject.asObservable();

  constructor(private http: HttpClient) {}

  fetch() {
    this.http.get<{ message: string }>(this.baseUrl).subscribe({
      next: (res) => {
        if (res.message) {
          this.messageSubject.next(res.message);
        }
      },
      error: () => {}
    });
  }

  clear() {
    this.messageSubject.next(null);
  }
}
