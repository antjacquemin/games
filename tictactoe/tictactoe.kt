package tictactoe

import java.util.Scanner
import kotlin.math.abs

fun showGrid(grid: CharArray) {
    println("-".repeat(9))
    println("| ${grid[0]} ${grid[1]} ${grid[2]} |")
    println("| ${grid[3]} ${grid[4]} ${grid[5]} |")
    println("| ${grid[6]} ${grid[7]} ${grid[8]} |")
    println("-".repeat(9))
}

fun isWinner(grid: CharArray, player: Char): Boolean {
    var win = false
    for (i in 0..2) {
        if (grid[3 * i] == player && grid[3 * i + 1] == player && grid[3 * i + 2] == player
            || grid[i] == player && grid[i + 3] == player && grid[i + 6] == player) {
                win = true
            }
    }
    if (grid[4] == player && (grid[0] == player && grid[8] == player || grid[2] == player && grid[6] == player)) {
        win = true
    }
    return win
}

fun main() {
    print("Enter cells: ")
    val scan = Scanner(System.`in`)
    val grid = scan.nextLine().toCharArray()
    showGrid(grid)
    /*
    if (abs(grid.count {c -> c == 'X'} - grid.count {c -> c == 'O'}) > 1) {
        println("Impossible")
    } else {
        val winX = isWinner(grid, 'X')
        val winO = isWinner(grid, 'O') 
        if (winX) {
            if (winO) {
                println("Impossible")
            } else {
                println("X wins")
            }
        } else if (winO) {
            println("O wins")
        } else if (grid.count {c -> c == '_'} > 0) {
            println("Game not finished")
        } else {
            println("Draw")
        }
    }*/
    var validInput = false
    var cellNumber = 0
    while (!validInput) {
        print("Enter the coordinates: ")
        var coord = readLine()!!.split(" ")
        var posX = coord[1].toIntOrNull()
        var posY = coord[0].toIntOrNull()
        if (posX == null || posY == null)
            println("You should enter numbers!")
        else if (posX > 3 || posX < 1 || posY > 3 || posY < 1)
            println("Coordinates should be from 1 to 3!")
        else {
            cellNumber = (posY - 1) * 3 + (posX - 1)
            if (grid[cellNumber] != '_')
                println("This cell is occupied! Choose another one!")
            else
                validInput = true
        }
        
    }
    grid[cellNumber] = 'X'
    showGrid(grid)
}