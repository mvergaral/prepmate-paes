import { NgModule } from '@angular/core';
import { IonicModule } from '@ionic/angular';
import { CommonModule } from '@angular/common';
import { LogoComponent } from './logo/logo.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ErrorBannerComponent } from './error-banner/error-banner.component';
import { NotificationBannerComponent } from './notification-banner/notification-banner.component';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [LogoComponent, NavbarComponent, ErrorBannerComponent, NotificationBannerComponent],
  imports: [CommonModule, RouterModule, IonicModule],
  exports: [LogoComponent, NavbarComponent, ErrorBannerComponent, NotificationBannerComponent]
})
export class ComponentsModule {}

