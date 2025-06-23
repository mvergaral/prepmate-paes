import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';
import { DashboardPageRoutingModule } from './dashboard-routing.module';
import { DashboardPage } from './dashboard.page';
import { ComponentsModule } from '../../components/components.module';

@NgModule({
  imports: [CommonModule, IonicModule, DashboardPageRoutingModule, ComponentsModule],
  declarations: [DashboardPage]
})
export class DashboardPageModule {}
