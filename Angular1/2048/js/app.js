'use strict';

var app = angular.module('wind_chimes', []);

app.controller('MainCtrl', ['$scope', '$timeout', function ($scope, $timeout) {
    $scope.data = [];
    $scope.score = 0;

    $scope.keypressed = function ($event) {
        switch ($event.keyCode) {
            case 37:
                $scope.mergeLeft();
                break;
            case 38:
                $scope.mergeUp();
                break;
            case 39:
                $scope.mergeRight();
                break;
            case 40:
                $scope.mergeDown();
                break;
        }
    }

    $scope.gameOver = false;
    $scope.isGameOver = function () {
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                if ($scope.data[i][j] === 0) {
                    return false;
                } else if (j < 3 && $scope.data[i][j] === $scope.data[i][j + 1]) {
                    return false;
                } else if (j > 0 && $scope.data[i][j] === $scope.data[i][j - 1]) {
                    return false;
                } else if (i < 3 && $scope.data[i][j] === $scope.data[i + 1][j]) {
                    return false;
                } else if (i > 0 && $scope.data[i][j] === $scope.data[i - 1][j]) {
                    return false;
                }
            }
        }
        $scope.gameOver = true;
    }

    $scope.startNewGame = function () {
        $scope.data = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ];
        $scope.score = 0;
        $scope.gameOver = false;
        $scope.setColors($scope.generateNewNum());
    }

    $scope.moveRight = function () {
        var moved = false;
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 3; j++) {
                if (!$scope.data[i][j + 1] && $scope.data[i][j]) {
                    //Move value to right
                    //After moving the value, fill the place with 0
                    $scope.data[i][j + 1] = $scope.data[i][j];
                    $scope.data[i][j] = 0;
                    moved = true;
                }
            }
        }
        if (moved) {
            $scope.moveRight();
        }
        return moved;
    }

    $scope._mergeRight = function () {
        var moved = false;
        moved = $scope.moveRight();
        for (let i = 0; i < 4; i++) {
            for (let j = 3; j > 0; j--) {
                if ($scope.data[i][j] === $scope.data[i][j - 1] && $scope.data[i][j]) {
                    $scope.data[i][j] *= 2;
                    $scope.score += $scope.data[i][j];
                    $scope.data[i][j - 1] = 0;
                    moved = true;
                }
            }
        }
        moved = $scope.moveRight(moved) || moved;
        return moved;
    }

    $scope.rotateClockwise = function (count) {
        for (let c = 0; c < count; c++) {
            var newArray = angular.copy($scope.data);
            for (let i = 0; i < 4; i++) {
                for (let j = 0; j < 4; j++) {
                    $scope.data[i][j] = newArray[3 - j][i];
                }
            }
        }
    }

    $scope.getValueForIndex = function (index) {
        return $scope.data[parseInt(index / 4)][index % 4];
    }

    $scope.generateNewNum = function () {
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 4; j++) {
                if ($scope.data[i][j] === 0) {
                    var place = Math.random();
                    var number = Math.random();
                    var num = 2;
                    if (number < 0.5) {
                        num = 4;
                    }
                    if (0.3 < place && place < 0.7) {
                        $scope.data[i][j] = num;
                        return [i, j];
                    } else {
                        continue;
                    }
                }
            }
        }
        return $scope.generateNewNum();
    }

    $scope.setColors = function (newNumPos) {
        $('#gaming_table td').each(function (index, value) {
            var color = 'white';
            var fontColor = 'black';
            if (index > 15) return;
            switch ($scope.getValueForIndex(index)) {
                case 2:
                    color = 'rgba(255, 255, 0, 0.35)';
                    break;
                case 4:
                    color = 'rgba(255, 255, 0, 0.7)';
                    break;
                case 8:
                    color = '#DAA520';
                    break;
                case 16:
                    color = '#ADFF2F';
                    break;
                case 32:
                    color = '#9ACD32';
                    break;
                case 64:
                    color = '#00FF7F';
                    break;
                case 128:
                    color = '#00CED1';
                    break;
                case 256:
                    color = '#1E90FF';
                    break;
                case 512:
                    color = '#0000FF';
                    break;
                case 1024:
                    color = '#808080';
                    break;
                case 2048:
                    color = '#8FBC8F';
                    break;
                case 5096:
                    color = '#9932CC';
                    break;
            }
            if (newNumPos && newNumPos[0] === parseInt(index / 4) && newNumPos[1] === index % 4) {
                color = 'black';
                fontColor = 'white';
            }
            $(this).css('background-color', color);
            $(this).css('color', fontColor);
        });
    }

    $scope.rotateAndMerge = function (c1, c2) {
        $scope.rotateClockwise(c1);
        var moved = $scope._mergeRight();
        $scope.rotateClockwise(c2);
        var newNumPos = undefined;
        if (moved) {
            var newNumPos = $scope.generateNewNum();
        }
        $scope.setColors(newNumPos);
        $scope.isGameOver();
    }

    $scope.mergeDown = function () {
        $scope.rotateAndMerge(3, 1);
    }

    $scope.mergeUp = function () {
        $scope.rotateAndMerge(1, 3);
    }

    $scope.mergeLeft = function () {
        $scope.rotateAndMerge(2, 2);
    }

    $scope.mergeRight = function () {
        $scope.rotateAndMerge(0, 0);
    }

    angular.element(document).ready(function () {
        $scope.startNewGame();
        $scope.$apply(function () { });
    });
}]);
