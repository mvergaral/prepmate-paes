import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ProfileService } from '../../services/profile.service';
import { ThemeService } from '../../services/theme.service';
import { REGIONS, Region } from '../../data/regions';

@Component({
  selector: 'app-profile-view',
  templateUrl: './profile-view.page.html',
  styleUrls: ['./profile-view.page.scss'],
  standalone: false
})
export class ProfileViewPage implements OnInit {
  user: any = null;
  editMode = false;
  profileForm: FormGroup;
  loading = false;
  errorMsg = '';
  successMsg = '';
  isDark = false;
  regions: Region[] = REGIONS;
  communes: string[] = [];

  constructor(
    private profile: ProfileService,
    private fb: FormBuilder,
    private theme: ThemeService
  ) {
    this.profileForm = this.fb.group({
      name: ['', Validators.required],
      rut: ['', Validators.required],
      colegio: [''],
      comuna: [''],
      region: [''],
      age: ['', Validators.required]
    });
    this.profileForm.get('region')?.valueChanges.subscribe(name => this.onRegionChange(name));
    this.isDark = this.theme.isDarkMode();
  }

  ngOnInit(): void {
    this.fetchProfile();
  }

  fetchProfile() {
    this.loading = true;
    this.profile.getProfile().subscribe({
      next: (res) => {
        this.user = res.student;
        this.profileForm.patchValue(this.user);
        if (this.user.region) {
          this.onRegionChange(this.user.region);
        }
        this.loading = false;
      },
      error: (err) => {
        this.errorMsg = err.error?.message || 'No se pudo cargar el perfil.';
        this.loading = false;
      }
    });
  }

  enableEdit() {
    this.editMode = true;
    this.successMsg = '';
    this.errorMsg = '';
  }

  cancelEdit() {
    this.editMode = false;
    this.profileForm.patchValue(this.user);
    this.successMsg = '';
    this.errorMsg = '';
  }

  toggleDarkMode() {
    this.theme.toggleTheme();
    this.isDark = this.theme.isDarkMode();
  }

  onSubmit() {
    if (this.profileForm.invalid) {
      this.errorMsg = 'Por favor completa todos los campos requeridos.';
      return;
    }
    this.loading = true;
    this.profile.updateProfile(this.profileForm.value).subscribe({
      next: (res) => {
        this.user = res.student;
        this.editMode = false;
        this.successMsg = 'Perfil actualizado correctamente.';
        this.loading = false;
      },
      error: (err) => {
        this.errorMsg = err.error?.message || 'Error al actualizar el perfil.';
        this.loading = false;
      }
    });
  }

  onRegionChange(name: string) {
    const region = this.regions.find(r => r.name === name);
    this.communes = region ? region.communes : [];
    if (!region) {
      this.profileForm.get('comuna')?.setValue('');
    }
  }
}
