# Telemetry

<p class="docs-audience">For: Game / backend engineer</p>

Telemetry is the **server-side logging of in-game events** (most importantly, the *game-open* session start) that TRACKS needs in order to attribute installs and in-game activity back to media campaigns. Without a telemetry backend that can reach the public internet, the Measurement API has nothing to receive.

## Option 1: We help you set up telemetry

If your game does not yet have a backend system for telemetry or event logging, our team can support you in setting one up—whether you're using **Unity** or **Unreal Engine**.

We provide guidance on:

- Integrating client-side telemetry scripts
- Sending key gameplay events (e.g. installs, level progress, purchases)
- Connecting telemetry to the TRACKS attribution pipeline

This ensures you can fully benefit from TRACKS' attribution and analytics capabilities.

> **Get in touch with us** to discuss telemetry setup options tailored to your game’s architecture.

## Option 2: The TRACKS plugin

If you do not have a telemetry pipeline and no capacity to build one before launch, a drop-in plugin sends the install signal and your custom events straight from the game client.

It is free on the Unity Asset Store. Setup is one config asset plus the endpoint and API key we issue for your title. There is no backend to run on your side.

[TRACKS Measurement SDK for Unity](https://assetstore.unity.com/packages/sdk/tracks-measurement-sdk-3740199)

**Unreal Engine** and **Godot** versions are available on request alongside your credentials.

> Not sure which suits you? **Talk to us first.** The answer usually depends on what your build pipeline already does rather than the size of your team.

## Next

Once telemetry is in place, wire in-game events into TRACKS through the [Measurement API](measurementapi.md) (see its [Integration approach](measurementapi.md#integration-approach) section for the expected payload fields).
