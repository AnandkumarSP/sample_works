import { Component, OnInit } from '@angular/core';

import { Hero } from './hero.model';
import { HeroComponent } from './hero.component';

import { HeroService } from './hero.service';

@Component({
    moduleId: module.id,
    selector: 'my-app',
    template: `
        <h1>{{name}}</h1>
        <router-outlet></router-outlet>
        <p>Create New Hero</p>
        <input type="text" [(ngModel)]="heroName" />
        <input type="number" [(ngModel)]="heroId" />
        <input type="button" value="Add Hero" (click)="addHero()" />
    `
})
export class AppComponent implements OnInit {
    name = 'Heros Application';
    heroName:string = '';
    heroId:number = 0;
    heros: Hero[];

    constructor(private heroService: HeroService) { }

    ngOnInit() {
        this.heros = this.heroService.getHeros();
    }

    addHero(): void {
        this.heroService.addHero(new Hero(this.heroId, this.heroName));
    }
}
