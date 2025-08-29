import { useEffect } from 'react';

/**
 * # Custom hook to dynamically update the document title.
 *
 * This hook sets the browser tab title whenever the component using it is mounted
 * or when the provided title changes. It prefixes the title with "DevMatch |" to
 * maintain consistent branding across pages.
 *
 * @param title - **(string)** The specific page title to append after the brand prefix.
 */
export function useDocumentTitle(title: string) {
  useEffect(() => {
    document.title = `DevMatch | ${title}`;
  }, [title]);
}
