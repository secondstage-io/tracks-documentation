---
description: "The three parts of a TRACKS Attribution integration: a telemetry backend, a measurement endpoint for game-open events, and postbacks to the ad platforms."
---

# Attribution Integration

TRACKS Attribution integrates with your game infrastructure through three components: a telemetry backend, a measurement endpoint that records game-open events, and postbacks that feed conversion signals back to your media platforms. A GDPR-compliant handling layer sits on top. Follow the paths below in order, or jump to the piece you need.

!!! note

    This section assumes the cloud environment is already provisioned. If it isn't, start with [Platform → Cloud Setup](../platform/cloud.md).

<section class="docs-home__journeys" aria-label="Attribution integration paths">

  <div class="journey-card">
    <div class="journey-card__head">
      <span class="journey-card__eyebrow">01 · Measurement</span>
      <h2 class="journey-card__title"><a href="../measurementapi/">Record events</a></h2>
      <p class="journey-card__audience">Wire game-open events from your telemetry backend into TRACKS through the Measurement API.</p>
    </div>
    <ol class="journey-card__steps">
      <li><a href="../telemetry/">Telemetry Setup</a></li>
      <li><a href="../measurementapi/">TRACKS Measurement API</a></li>
    </ol>
    <div class="journey-card__foot">
      <a class="journey-card__primary" href="../telemetry/">Start with Telemetry →</a>
    </div>
  </div>

  <div class="journey-card">
    <div class="journey-card__head">
      <span class="journey-card__eyebrow">02 · Postbacks</span>
      <h2 class="journey-card__title"><a href="../postbacks/">Send signals back</a></h2>
      <p class="journey-card__audience">Close the loop by sending install and in-game events back to your media platforms through their Conversion APIs.</p>
    </div>
    <ol class="journey-card__steps">
      <li><a href="../postbacks/meta/">Meta</a></li>
      <li><a href="../postbacks/google/">Google Ads</a></li>
      <li><a href="../postbacks/">Other platforms</a></li>
    </ol>
    <div class="journey-card__foot">
      <a class="journey-card__primary" href="../postbacks/">Go to Postbacks →</a>
    </div>
  </div>

  <div class="journey-card">
    <div class="journey-card__head">
      <span class="journey-card__eyebrow">03 · Compliance</span>
      <h2 class="journey-card__title"><a href="../gdprapi/">Stay GDPR-compliant</a></h2>
      <p class="journey-card__audience">Give users the right to be forgotten and meet EU data-handling obligations through the GDPR API.</p>
    </div>
    <ol class="journey-card__steps">
      <li><a href="../gdprapi/">GDPR API</a></li>
    </ol>
    <div class="journey-card__foot">
      <a class="journey-card__primary" href="../gdprapi/">Integrate the GDPR API →</a>
    </div>
  </div>

</section>
