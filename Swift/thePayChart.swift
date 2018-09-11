
let employees = [(100, "John", 35.0, 0.0, 0.0, 3),
                 (132, "Mark", 40.0, 5.0, 0.0, 2),
                 (210, "Susan", 40.0, 0.0, 0.0, 2),
                 (155, "Blake", 40.0, 20.0, 0.0, 1),
                 (349, "Thomas", 40.0, 5.0, 0.0, 2),
                 (349, "Connor", 40.0, 2.0, 3.0, 4),
                 (240, "Teri", 40.0, 5.0, 5.0, 2)]


// Employee pay scale should be used as key values for the hourlyWage dictionary.
let hourlyWage = [1: 25.00, 2: 31.50, 3: 38.25, 4: 44.75]
let overtimeRateMultiplier = 1.5
let holidayRateMultiplier = 2.0

let johnPay = employees[0].2 * hourlyWage[4]


let myASCIIBox =
 """
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│  ID  ║  Name  ║  Regular Hours  ║  Overtime Hours  ║  Holiday Hours  ║  Pay Scale  │  Amt Earned  │
│══════╩════════╩═════════════════╩══════════════════╩═════════════════╩════════════════════════════│
│\(String(employees[0].0).padding(toLength:6, withPad: " ", startingAt: 0))│\(String(employees[0].1).padding(toLength:8, withPad: " ", startingAt: 0))│\(String(employees[0].2).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[0].3).padding(toLength:18, withPad: " ", startingAt: 0))│\(String(employees[0].4).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[0].5).padding(toLength:13, withPad: " ", startingAt: 0))│$\(String(johnPay).padding(toLength:13, withPad: " ", startingAt: 0))│
│───────────────────────────────────────────────────────────────────────────────────────────────────│
│\(String(employees[1].0).padding(toLength:6, withPad: " ", startingAt: 0))│\(String(employees[1].1).padding(toLength:8, withPad: " ", startingAt: 0))│\(String(employees[1].2).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[1].3).padding(toLength:18, withPad: " ", startingAt: 0))│\(String(employees[1].4).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[1].5).padding(toLength:13, withPad: " ", startingAt: 0))│$\(String(markPay).padding(toLength:13, withPad: " ", startingAt: 0))│
│───────────────────────────────────────────────────────────────────────────────────────────────────│
│\(String(employees[2].0).padding(toLength:6, withPad: " ", startingAt: 0))│\(String(employees[2].1).padding(toLength:8, withPad: " ", startingAt: 0))│\(String(employees[2].2).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[2].3).padding(toLength:18, withPad: " ", startingAt: 0))│\(String(employees[2].4).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[2].5).padding(toLength:13, withPad: " ", startingAt: 0))│$\(String(susanPay).padding(toLength:13, withPad: " ", startingAt: 0))│
│───────────────────────────────────────────────────────────────────────────────────────────────────│
│\(String(employees[3].0).padding(toLength:6, withPad: " ", startingAt: 0))│\(String(employees[3].1).padding(toLength:8, withPad: " ", startingAt: 0))│\(String(employees[3].2).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[3].3).padding(toLength:18, withPad: " ", startingAt: 0))│\(String(employees[3].4).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[3].5).padding(toLength:13, withPad: " ", startingAt: 0))│$\(String(blakePay).padding(toLength:13, withPad: " ", startingAt: 0))│
│───────────────────────────────────────────────────────────────────────────────────────────────────│
│\(String(employees[4].0).padding(toLength:6, withPad: " ", startingAt: 0))│\(String(employees[4].1).padding(toLength:8, withPad: " ", startingAt: 0))│\(String(employees[4].2).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[4].3).padding(toLength:18, withPad: " ", startingAt: 0))│\(String(employees[4].4).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[4].5).padding(toLength:13, withPad: " ", startingAt: 0))│$\(String(thomasPay).padding(toLength:13, withPad: " ", startingAt: 0))│
│───────────────────────────────────────────────────────────────────────────────────────────────────│
│\(String(employees[5].0).padding(toLength:6, withPad: " ", startingAt: 0))│\(String(employees[5].1).padding(toLength:8, withPad: " ", startingAt: 0))│\(String(employees[5].2).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[5].3).padding(toLength:18, withPad: " ", startingAt: 0))│\(String(employees[5].4).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[5].5).padding(toLength:13, withPad: " ", startingAt: 0))│$\(String(connorPay).padding(toLength:13, withPad: " ", startingAt: 0))│
│───────────────────────────────────────────────────────────────────────────────────────────────────│
│\(String(employees[6].0).padding(toLength:6, withPad: " ", startingAt: 0))│\(String(employees[6].1).padding(toLength:8, withPad: " ", startingAt: 0))│\(String(employees[6].2).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[6].3).padding(toLength:18, withPad: " ", startingAt: 0))│\(String(employees[6].4).padding(toLength:17, withPad: " ", startingAt: 0))│\(String(employees[6].5).padding(toLength:13, withPad: " ", startingAt: 0))│$\(String(teriPay).padding(toLength:13, withPad: " ", startingAt: 0))│
│───────────────────────────────────────────────────────────────────────────────────────────────────│
│                                                                                    │              │
│                                                                              TOTAL:│$\(String(total).padding(toLength:13, withPad: " ", startingAt: 0))│
└───────────────────────────────────────────────────────────────────────────────────────────────────┘
"""
