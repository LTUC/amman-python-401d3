# Lab: React 2

## Overview

- Create a ReactJS web application that displays a list of things, and allows creating new things.

## Feature Tasks and Requirements

- Create a web app with a top level `App` component
  - `App` component should...
    - have `thingList` data stored in its state.
    - render 3 nested components
      - `Header`
      - `ThingList`
      - `Footer`
  - `thingList` should be an array of plain old JavaScript objects (aka POJO) that represent a thing that has a name.
    - E.g. {name:'rake'}
  - `Header` component should...
    - receive a `things count` as a prop
    - display a heading
    - display the current count of things
  - `ThingList` component should...
    - receive a `list of things` as a prop
    - receive a function to call when a new `thing` is created.
    - Display an unordered list composed of `ThingItem` components
    - Display a form that allows creation of a `thing`
    - When user creates new `thing` the rest of application should update appropriately.
      - `Header` thing count should update
      - `ThingList` should add a new `ThingItem` to end of list
  - `ThingItem` component should...
    - receive a `name` as a prop
  - `Footer` component should...
    - Display some placeholder text (e.g. lorem ipsum)

## Implementation Notes

- `npx create-react-app thing-creator`
- follow terminal instructions

## Stretch Goals

- read in `things` data from an external JSON file
- Use a hooks based form

### User Acceptance Tests

No acceptance tests required

## Configuration

- create `react-things` repository on Github

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.
