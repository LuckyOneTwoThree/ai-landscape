'use client'

import { useEffect, useState } from 'react'

interface TOCItem {
  id: string
  text: string
  level: number
}

export default function TableOfContents({ locale = 'zh' }: { locale?: string }) {
  const [headings, setHeadings] = useState<TOCItem[]>([])
  const [activeId, setActiveId] = useState<string>('')

  useEffect(() => {
    // Give time for the article to render
    const timeout = setTimeout(() => {
      const elements = Array.from(document.querySelectorAll('article h2, article h3'))
      
      const items: TOCItem[] = elements.map((elem) => ({
        id: elem.id,
        text: (elem as HTMLElement).innerText.replace(/^#\s*/, ''),
        level: Number(elem.tagName.substring(1))
      })).filter(item => item.id)
      
      setHeadings(items)

      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              setActiveId(entry.target.id)
            }
          })
        },
        { rootMargin: '0px 0px -80% 0px' }
      )

      elements.forEach((elem) => observer.observe(elem))
      
      return () => observer.disconnect()
    }, 100)

    return () => clearTimeout(timeout)
  }, [])

  if (headings.length === 0) return null

  return (
    <div style={{
      fontSize: '0.85rem',
      color: 'var(--text-secondary)'
    }}>
      <div style={{
        fontWeight: 600,
        color: 'var(--text-primary)',
        marginBottom: '1rem',
        textTransform: 'uppercase',
        letterSpacing: '0.05em'
      }}>
        {locale === 'en' ? 'On this page' : '本页目录'}
      </div>
      <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '0.6rem' }}>
        {headings.map(heading => (
          <li key={heading.id} style={{ 
            paddingLeft: heading.level === 3 ? '1rem' : '0' 
          }}>
            <a 
              href={`#${heading.id}`}
              style={{
                color: activeId === heading.id ? 'var(--text-primary)' : 'inherit',
                textDecoration: 'none',
                transition: 'color 0.2s',
                display: 'block',
                borderLeft: activeId === heading.id ? '2px solid var(--text-primary)' : '2px solid transparent',
                paddingLeft: '10px',
                marginLeft: '-12px'
              }}
              onMouseEnter={(e) => { e.currentTarget.style.color = 'var(--text-primary)' }}
              onMouseLeave={(e) => { if (activeId !== heading.id) e.currentTarget.style.color = 'var(--text-secondary)' }}
              onClick={(e) => {
                e.preventDefault()
                document.getElementById(heading.id)?.scrollIntoView({ behavior: 'smooth' })
                window.history.pushState(null, '', `#${heading.id}`)
                setActiveId(heading.id)
              }}
            >
              {heading.text}
            </a>
          </li>
        ))}
      </ul>
    </div>
  )
}
