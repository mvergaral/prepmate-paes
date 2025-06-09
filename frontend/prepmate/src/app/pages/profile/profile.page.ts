import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ProfileService } from '../../services/profile.service';

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
    private profile: ProfileService
  ) {
    this.profileForm = this.fb.group({
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
    this.profile.updateProfile(this.profileForm.value).subscribe({
      next: () => {
        this.loading = false;
        this.router.navigate(['/profile/view']);
      },
      error: (err) => {
        this.loading = false;
        this.errorMsg = 'Error al guardar el perfil.';
      }
    });
  }
}
