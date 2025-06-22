import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LogoComponent } from './logo/logo.component';
import { NavbarComponent } from './navbar/navbar.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [LogoComponent, NavbarComponent],
  imports: [CommonModule, RouterModule],
  exports: [LogoComponent, NavbarComponent]
})
export class ComponentsModule {}