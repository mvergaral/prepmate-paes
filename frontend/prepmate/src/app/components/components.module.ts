import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LogoComponent } from './logo/logo.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [LogoComponent],
  imports: [CommonModule, RouterModule],
  exports: [LogoComponent]
})
export class ComponentsModule {}