'use client'

import { useEffect, useRef } from 'react'
import mermaid from 'mermaid'
import { useTheme } from 'next-themes'

export default function MarkdownViewer({ contentHtml }: { contentHtml: string }) {
  const { resolvedTheme } = useTheme()
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    // Initialize mermaid with the current theme
    mermaid.initialize({ 
      startOnLoad: false, 
      theme: resolvedTheme === 'dark' ? 'dark' : 'default',
      securityLevel: 'loose'
    })
    
    if (containerRef.current) {
      // Find all code blocks that have the language-mermaid class
      const elements = containerRef.current.querySelectorAll('.language-mermaid')
      if (elements.length > 0) {
        // Run mermaid on these specific nodes
        mermaid.run({
          nodes: Array.from(elements) as HTMLElement[],
          suppressErrors: true
        }).catch(console.error)
      }
    }
  }, [contentHtml, resolvedTheme])

  return (
    <div 
      // Using resolvedTheme as key forces React to completely unmount and remount 
      // the div when the theme changes. This restores the original <pre><code> 
      // tags so Mermaid can re-render them with the new theme!
      key={resolvedTheme} 
      ref={containerRef}
      dangerouslySetInnerHTML={{ __html: contentHtml }} 
      className="mermaid-container"
    />
  )
}
