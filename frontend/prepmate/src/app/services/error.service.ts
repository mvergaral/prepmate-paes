import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ErrorService {
  private messageSubject = new BehaviorSubject<string | null>(null);
  message$ = this.messageSubject.asObservable();

  show(message: string) {
    this.messageSubject.next(message);
  }

  clear() {
    this.messageSubject.next(null);
  }

  handle(err: any, fallback = 'Ocurrió un error de conexión.') {
    const msg = err?.error?.message || err?.message || fallback;
    this.show(msg);
  }
}
