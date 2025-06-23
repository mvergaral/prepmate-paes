import { Injectable } from '@angular/core';
import {
  HttpEvent,
  HttpHandler,
  HttpInterceptor,
  HttpRequest,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { TokenService } from './token.service';
import { Router } from '@angular/router';
import { ErrorService } from './error.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(private tokenService: TokenService, private router: Router, private error: ErrorService) {}

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const token = this.tokenService.getToken();
    let authReq = req;
    if (token) {
      authReq = req.clone({
        setHeaders: { Authorization: `Bearer ${token}` }
      });
    }
    return next.handle(authReq).pipe(
      catchError((error: HttpErrorResponse) => {
        const loginOrSignup = authReq.url.endsWith('/auth/login') || authReq.url.endsWith('/auth/signup');
        if (error.status === 401 && !loginOrSignup) {
          this.tokenService.removeToken();
          this.router.navigate(['/login']);
          this.error.show(error.error?.message || 'Sesión expirada. Por favor inicia sesión nuevamente.');
        } else {
          this.error.show(error.error?.message || 'Ocurrió un error de conexión.');
        }
        return throwError(() => error);
      })
    );
  }
}
