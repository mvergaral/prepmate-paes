import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { AuthStore } from '../../store/auth.store';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
  standalone: false
})
export class LoginPage {
  loginForm: FormGroup;

  constructor(private fb: FormBuilder, private auth: AuthService, private store: AuthStore, private router: Router) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
    });
  }

  onSubmit() {
    if (this.loginForm.invalid) {
      console.log('❌ Formulario inválido');
      return;
    }

    this.auth.login(this.loginForm.value).subscribe({
      next: (res) => {
        this.store.setSession(res);
        this.router.navigate(['/profile/view']);
      },
      error: (err) => {
        console.error('❌ Error en login', err);
      }
    });
  }
}
