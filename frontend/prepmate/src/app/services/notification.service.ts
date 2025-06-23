import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ToastService } from './toast.service';
import { environment } from '../../environments/environment';

@Injectable({ providedIn: 'root' })
export class NotificationService {
  private baseUrl = environment.apiUrl + '/api/notifications';

  constructor(private http: HttpClient, private toast: ToastService) {}

  fetch() {
    this.http.get<{ message: string }>(this.baseUrl).subscribe({
      next: (res) => {
        if (res.message) {
          this.toast.show(res.message);
        }
      },
      error: () => {}
    });
  }
}
