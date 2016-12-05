
type characters = '' | 'SUPERMAN' | 'IRONMAN' | 'HULK' | string;

export class Hero {
    showDetails: boolean = false;

    constructor (public id=0, public name="DefaultName", public character="") {
        this.showDetails = false;
    }
}