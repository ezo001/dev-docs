/**
 * DocItem Footer: adds "Report a problem" link above "Edit this page".
 */
import React from 'react';
import clsx from 'clsx';
import {ThemeClassNames} from '@docusaurus/theme-common';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import TagsListInline from '@theme/TagsListInline';
import EditMetaRow from '@theme/EditMetaRow';

const REPORT_PROBLEM_URL = 'https://forms.office.com/r/VzvB13HvFE';

export default function DocItemFooter() {
  const {metadata} = useDoc();
  const {editUrl, lastUpdatedAt, lastUpdatedBy, tags} = metadata;
  const canDisplayTagsRow = tags.length > 0;
  const canDisplayEditMetaRow = !!(editUrl || lastUpdatedAt || lastUpdatedBy);
  const canDisplayFooter =
    canDisplayTagsRow || canDisplayEditMetaRow || true; // Always show footer for "Report a problem"
  if (!canDisplayFooter) {
    return null;
  }
  return (
    <footer
      className={clsx(ThemeClassNames.docs.docFooter, 'docusaurus-mt-lg')}>
      {/* Report a problem link - above Edit this page */}
      <div
        className={clsx(
          'row margin-bottom--sm',
          ThemeClassNames.docs.docFooterEditMetaRow,
        )}>
        <div className="col">
          <a
            href={REPORT_PROBLEM_URL}
            target="_blank"
            rel="noopener noreferrer"
            className={ThemeClassNames.common.editThisPage}
          >
            Report a problem
          </a>
        </div>
      </div>
      {canDisplayTagsRow && (
        <div
          className={clsx(
            'row margin-top--sm',
            ThemeClassNames.docs.docFooterTagsRow,
          )}>
          <div className="col">
            <TagsListInline tags={tags} />
          </div>
        </div>
      )}
      {canDisplayEditMetaRow && (
        <EditMetaRow
          className={clsx(
            'margin-top--sm',
            ThemeClassNames.docs.docFooterEditMetaRow,
          )}
          editUrl={editUrl}
          lastUpdatedAt={lastUpdatedAt}
          lastUpdatedBy={lastUpdatedBy}
        />
      )}
    </footer>
  );
}
