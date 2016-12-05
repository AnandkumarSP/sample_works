import { Component, Input } from '@angular/core';

import { Hero } from './hero.model';
import { HeroService } from './hero.service';

@Component({
    moduleId: module.id,
    selector: 'hero-component',
    template: `
    <div class="hero-component" *ngFor='let hero of heros'
            (mouseenter)="setDetailsButtonVisibility(hero)"
            (mouseleave)="setDetailsButtonVisibility()">
        <p>ID: {{hero.id}}</p>
        <p>{{hero.name}}</p>
        <input type="button" value="Remove Hero" (click)="removeHero(hero)" />
        <input type="button" [value]="hero.showDetails ? 'Hide Details' : 'Show Details'"
            *ngIf="hero === activeHero" (click)="hero.showDetails = !hero.showDetails" />
        <div *ngIf="hero.showDetails">
            <p>Character: {{hero.character}}</p>
        </div>
    </div>
    `,
    styles: [`
        div.hero-component {
            border: 1px solid black;
        }
    `]
})
export class HeroComponent {
    heros: Hero[];
    activeHero: Hero;
    showDetailsButton: boolean = false;

    constructor(private heroService: HeroService) { }

    ngOnInit() {
        this.heros = this.heroService.getHeros();
        console.log(this);
    }

    removeHero(hero: Hero): void {
        this.heroService.removeHero(hero);
    }

    setDetailsButtonVisibility(hero: Hero): void {
        this.activeHero = hero;
    }
}