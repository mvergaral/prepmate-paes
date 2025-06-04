import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { AuthStore } from '../../store/auth.store';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.page.html',
  standalone: false
})
export class SignupPage {
  signupForm: FormGroup;

  private passwordMatchValidator(form: FormGroup) {
    const password = form.get('password')?.value;
    const confirmPassword = form.get('confirmPassword')?.value;
    return password === confirmPassword ? null : { passwordMismatch: true };
  }

  constructor(private fb: FormBuilder, private router: Router, private auth: AuthService, private store: AuthStore) {
    this.signupForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      confirmPassword: ['', Validators.required],
      terms: [false, Validators.requiredTrue]
    }, {
      validators: this.passwordMatchValidator
    });
  }

  onSubmit() {
    if (this.signupForm.invalid) {
      console.log('❌ Formulario inválido');
      return;
    }

    const { email, password, terms } = this.signupForm.value;
    this.auth.signup({ email, password, terms }).subscribe({
      next: (res) => {
        this.store.setSession(res);
        this.router.navigate(['/profile']);
      },
      error: (err) => {
        console.error('❌ Error en registro', err);
      }
    });
  }
}
