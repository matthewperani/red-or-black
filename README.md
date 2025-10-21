# Red or Black?

## Guess the color of the suit to win!

To play:

First start the dealer server:

```
$ python3 server.py
```

Then start the client (player) in another terminal:

```
$ python3 client.py
```

Roadmap:
- Ability to serve multiple connections at once, each with their own game
- Containerized server 
- Keep track of score for round
    - keep track of highest score for that session
        - keep track of highest score for all sessions 
            - perhaps a containerized database that runs alongside the server