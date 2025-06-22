import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SubjectSelectPage } from './subject-select.page';

const routes: Routes = [
  {
    path: '',
    component: SubjectSelectPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class SubjectSelectPageRoutingModule {}
