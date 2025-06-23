import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';
import { SessionPageRoutingModule } from './session-routing.module';
import { SessionPage } from './session.page';
import { ComponentsModule } from '../../components/components.module';

@NgModule({
  imports: [CommonModule, FormsModule, IonicModule, SessionPageRoutingModule, ComponentsModule],
  declarations: [SessionPage]
})
export class SessionPageModule {}
