import { Component, Input } from '@angular/core';

import { Hero } from './hero.model';
import  { HeroService } from './hero.service';

@Component({
    selector: 'hero-component',
    template: `
    <div class="hero-component" (mouseenter)="setDetailsButtonVisibility(true)" (mouseleave)="setDetailsButtonVisibility(false)">
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
    @Input() hero:Hero;
    showDetailsButton:boolean = false;
    showDetails:boolean = false;

    constructor(private heroService:HeroService) { }

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