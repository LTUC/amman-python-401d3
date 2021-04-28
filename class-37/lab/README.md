# Lab: React 1

## Overview

Create an Odometer web page using ReactJS.

## Feature Tasks and Requirements

- Display an odometer with 4 digits
  - Pad with zeroes as needed (e.g. 0045)
    - JavaScript has a method for this. Research as needed.
- Add buttons to increment the "miles" by 1, 10, 100 and 1000.
  - Roll over when odometer value exceeds 9999
  - Maintain any "extra" amount when rolling over.
- The root `App` component should contain `Odometer`,`Header` and `Footer` components.
  - You decide when appropriate to use class based or functional components.
  - `Header` component should receive a `text` value via props.
  - `Footer` component should receive a `trademark` value via props.
  - `Odometer` component should store numeric value in it's state.
    - Remember to update state in the React way.

## Implementation Notes

- `npx create-react-app odometer`
- follow instruction in terminal

### User Acceptance Tests

No testing required.

## Configuration

Create `odometer` repository in Github

Use the folder created by `create-react-app` as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.

### Stretch Goals

- Refactor to move components to own files.
- Add more styling
- Store odometer's state in `App` component while keeping UI logic in separate `Odometer` component.
