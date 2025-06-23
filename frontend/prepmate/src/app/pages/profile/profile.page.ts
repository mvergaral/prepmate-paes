import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ProfileService } from '../../services/profile.service';
import { REGIONS, Region } from '../../data/regions';

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
  regions: Region[] = REGIONS;
  communes: string[] = [];

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

    this.profileForm.get('region')?.valueChanges.subscribe(regionName => {
      const region = this.regions.find(r => r.name === regionName);
      this.communes = region ? region.communes : [];
      this.profileForm.get('comuna')?.setValue('');
    });
  }

  ngOnInit(): void {
    const regionName = this.profileForm.get('region')?.value;
    if (regionName) {
      const region = this.regions.find(r => r.name === regionName);
      this.communes = region ? region.communes : [];
    }
  }

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
        this.errorMsg = err.error?.message || 'Error al guardar el perfil.';
      }
    });
  }
}
