# Demo → Full Game Conversion

<p class="docs-audience">For: UA and marketing leads, producers</p>

These metrics show how many players who tried the demo went on to buy and launch the full game, and which acquisition channels brought in the demo players most likely to convert.

## Metrics

| Metric | Definition |
| --- | --- |
| **Demo-to-FullGame Converters** | The number of players who played the demo first and later launched the full game |
| **Demo-to-FullGame CVR %** | Converters as a share of all demo players |

For example, 1,000 demo players and 170 converters give a CVR of 17%.

## Player types

Every player falls into one of three groups:

| Player type | Meaning |
| --- | --- |
| **Demo only** | Played the demo and hasn't bought the full game (yet) |
| **Demo → FullGame** | Played the demo, then bought and launched the full game |
| **FullGame direct** | Bought the full game without playing the demo first |

## How to read it

- **Date range.** By default the report groups players by the day they first installed (for converters, that is the demo install). A cohort's CVR can keep rising for a few weeks after its install date, because many players buy later. Recent cohorts will look lower until they mature.
- **Channel.** A converter is credited to the channel that brought them to the demo. This shows which campaigns brought in demo players who went on to buy.

!!! tip "Compare cohorts of the same age"

    Because conversion keeps growing for weeks, compare a recent week's CVR with older weeks only once it has had the same time to mature.

## What we need from the studio

Conversion tracking only works if the game sends consistent data:

<ol class="setup-steps" markdown="1">

<li markdown="block">

### The same player ID in the demo and the full game

A player's ID must stay the same when they move from the demo to the full game on the same account and platform. If the full game creates a new ID, the player looks like a brand-new install and the conversion is lost.

</li>

<li markdown="block">

### Clear version labels

The demo build should report a version that includes "Demo" (for example `1.0.4-Demo`). The full game should report a plain version (for example `1.0.4`). Please keep this naming in all future patches of both builds.

</li>

<li markdown="block">

### A first-launch flag

Both builds should mark a player's very first launch, so we can tell new installs from returning players.

</li>

</ol>

## Related

- [Player Lifecycle](player-lifecycle.md): retention and churn, with a Version filter to separate demo and full-game players.
- [Telemetry Setup](../attribution/telemetry.md): how builds send events to TRACKS.
- [Conversions & Audiences](../attribution/postbacks/conversions-audiences.md): sending demo installs to ad platforms.
