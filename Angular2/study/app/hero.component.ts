import { Component, Input } from '@angular/core';

import { Hero } from './hero.model';
import  { HeroService } from './hero.service';

@Component({
    moduleId: module.id,
    selector: 'hero-component',
    template: `
    <div class="hero-component" *ngFor='let hero of heros' (mouseenter)="setDetailsButtonVisibility(true)" (mouseleave)="setDetailsButtonVisibility(false)">
        <p>ID: {{hero.id}}</p>
        <p>{{hero.name}}</p>
        <input type="button" value="Remove Hero" (click)="removeHero(hero)" />
        <input type="button" [value]="showDetails ? 'Hide Details' : 'Show Details'"
            *ngIf="showDetailsButton" (click)="toggleDetailsVisibility()" />
        <div *ngIf="showDetails">
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
    showDetailsButton:boolean = false;
    showDetails:boolean = false;
    heros: Hero[];

    constructor(private heroService:HeroService) { }

    ngOnInit() {
        this.heros = this.heroService.getHeros();
    }

    removeHero(hero:Hero) :void {
        this.heroService.removeHero(hero);
    }

    setDetailsButtonVisibility(show:boolean): void {
        this.showDetailsButton = show;
        if (!show) this.showDetails = false;
    }

    toggleDetailsVisibility(): void {
        this.showDetails = !this.showDetails;
    }
}