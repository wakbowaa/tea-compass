# FLIGHT CARD TC-01

**Tea:** Tea Compass  
**Purpose:** Build one shared sensory profile without letting the host decide which language becomes canonical.

## Leaf and water

A host binds origin notes, preparation, and three to six descriptor families into a StudioNet flight. Every wallet may taste once. An accepted note fills exactly one open leaf. Three rejected notes wash the flight out; one accepted note in every family produces `PROFILED`.

## Fold rules

`open_flight` rejects duplicate IDs, thin preparation notes, and weak vocabularies before storage. `pin_note` requires an active flight, an open allowed family, a unique taster, and substantive grounding before consensus.

The jury asks whether the descriptor is plausible for the frozen origin and preparation, belongs to the selected family, and differs from every accepted note. A second validator independently checks that substance. Code then rejects mismatched families, duplicates, and issue-bearing decisions before changing state.

The frontend reads `get_flight`, `get_reviews_page`, `get_flights_page`, and `get_summary`. No private database holds the shared palate.

## Shared palate

The interface is a folding paper instrument, not a submission feed. AromaFan, SteamCup, SteepLedger, TastingSlip, FatigueWash, and TransactionSeam expose the state machine directly. Steam Curl, Leaf Unfold, Ink Soak, Palate Wash, and Binding Settle give each lifecycle change its own motion.

GenLayer is load-bearing because sensory fit, family placement, and synonym-level duplication need contextual judgment, while the accepted profile must be shared state rather than one host's preference.

## Steep commands

```text
genvm-lint lint contracts/contract.py
python -m pytest tests/test_surface.py -q
node scripts/no-emoji.js
node scripts/no-emdash.js
cd frontend
npm install
npm run typecheck
npm run build
```

Set `NEXT_PUBLIC_CONTRACT_ADDRESS` for a new deployment. The shipped static app talks directly to StudioNet through `genlayer-js`, pauses view refresh while a transaction is active, and otherwise refreshes no faster than every 90 seconds.

## Final rinse

**Contract:** `0x3b8dDEF7cD08764df66845a2E18D92B1D08C87D4`  
**Deployment:** `0xc9a246d47ec46770eb6a1f15c11a23649e4038032ae19aecfc7743ae4d5da317`  
**Repository:** https://github.com/wakbowaa/tea-compass  
**Public instrument:** https://tea-compass.pages.dev/

This is a cooperative vocabulary exercise. It does not determine product quality, chemical composition, health effects, origin authenticity, safety, or commercial grade. The StudioNet deployment finalized with `MAJORITY_AGREE` and leader execution `SUCCESS`.
