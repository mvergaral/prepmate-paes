import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.page.html',
  styleUrls: ['./profile.page.scss'],
  standalone: false
})
export class ProfilePage implements OnInit {
  profileForm: FormGroup;
  loading = false;
  errorMsg = '';

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private http: HttpClient
  ) {
    this.profileForm = this.fb.group({
      nombre: ['', Validators.required],
      rut: ['', Validators.required],
      colegio: ['', Validators.required],
      comuna: ['', Validators.required],
      region: ['', Validators.required]
    });
  }

  ngOnInit(): void {}

  onSubmit() {
    if (this.profileForm.invalid) {
      this.errorMsg = 'Por favor completa todos los campos.';
      return;
    }
    this.loading = true;
    this.errorMsg = '';
    // Simulación de obtención de token JWT (ajusta según tu auth real)
    const token = localStorage.getItem('jwt_token');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${token}`
    });
    this.http.post('/api/profile', this.profileForm.value, { headers }).subscribe({
      next: () => {
        this.loading = false;
        // Redirigir o mostrar mensaje de éxito
        this.router.navigate(['/home']);
      },
      error: (err) => {
        this.loading = false;
        this.errorMsg = 'Error al guardar el perfil.';
      }
    });
  }
}
