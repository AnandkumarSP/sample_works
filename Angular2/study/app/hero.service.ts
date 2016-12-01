import { Injectable } from '@angular/core';

import { Hero } from './hero.model';

@Injectable()
export class HeroService {
    heros:Hero[] = [{
        id: 1,
        name: 'Hero 1',
        character: 'SUPERMAN'
    }];

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