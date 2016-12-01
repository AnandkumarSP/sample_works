
type characters = '' | 'SUPERMAN' | 'IRONMAN' | 'HULK' | string;

export class Hero {
    constructor (public id=0, public name="DefaultName", public character="") { }
}