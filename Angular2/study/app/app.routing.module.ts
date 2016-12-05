import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

import { HeroComponent } from './hero.component';

@NgModule({
    imports: [
        RouterModule.forRoot([
            {
                path: "heroes",
                component: HeroComponent
            },
            {
                path: "",
                redirectTo: "/heroes",
                pathMatch: "full"
            }])
    ]
})
export class RoutingModule { }