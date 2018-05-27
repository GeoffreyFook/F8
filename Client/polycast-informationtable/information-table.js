import {html, PolymerElement} from '@polymer/polymer/polymer-element.js';

/**
 * `information-table`
 * displays some information
 *
 * @customElement
 * @polymer
 * @demo demo/index.html
 */
class InformationTable extends PolymerElement {
  static get template() {
    return html`
      <style>
        :host {
          display: block;
        }
      </style>
      <h2>Hello [[prop1]]!</h2>
    `;
  }
  static get properties() {
    return {
      prop1: {
        type: String,
        value: 'information-table',
      },
    };
  }
}

window.customElements.define('information-table', InformationTable);
