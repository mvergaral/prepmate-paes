import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';
import { ExercisePageRoutingModule } from './exercise-routing.module';
import { ExercisePage } from './exercise.page';
import { ComponentsModule } from '../../components/components.module';

@NgModule({
  imports: [CommonModule, FormsModule, IonicModule, ExercisePageRoutingModule, ComponentsModule],
  declarations: [ExercisePage]
})
export class ExercisePageModule {}
