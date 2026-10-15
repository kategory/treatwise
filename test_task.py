import task

def test_reward():
    t = task.Tasks(
        (
            task.Task( "2026-04-16", "Einkaufsliste prüfen", "Offen", 10 ),
            task.Task( "2026-04-16", "Taschen packen", "Fertig", 15),
            task.Task( "2026-04-17", "Hausaufgaben kontrollieren", "Offen", 5),
        )
    )

    assert t.reward() == 15


# Application <-- Integration test

# windows and GUI elements <-- Integration test

# complex functions

# module

# classes  <-- Unit test

# methods  <-- Unit test

# functions <-- Unit test