import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { IonicModule } from '@ionic/angular';

import { ProfilePageRoutingModule } from './profile-routing.module';
import { ComponentsModule } from '../../components/components.module';

import { ProfilePage } from './profile.page';
import { ProfileViewPage } from './profile-view.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    IonicModule,
    ProfilePageRoutingModule,
    ComponentsModule,
    HttpClientModule
  ],
  declarations: [ProfilePage, ProfileViewPage]
})
export class ProfilePageModule {}
