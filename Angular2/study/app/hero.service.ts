import { Injectable } from '@angular/core';

import { Hero } from './hero.model';

@Injectable()
export class HeroService {
    heros:Hero[] = [new Hero(1, 'Hero 1', 'SUPERMAN')];

    getHeros(): Hero[] {
        return this.heros;
    }

    addHero(hero:Hero): void {
        this.heros.push(hero);
    }

    removeHero(hero:Hero): void {
        this.heros.splice(this.heros.indexOf(hero), 1);
    }
}