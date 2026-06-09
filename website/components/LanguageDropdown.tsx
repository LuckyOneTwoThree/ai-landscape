'use client'

import React, { useState, useRef, useEffect } from 'react'
import { usePathname, useRouter } from 'next/navigation'

export default function LanguageDropdown() {
  const pathname = usePathname()
  const router = useRouter()
  const [isOpen, setIsOpen] = React.useState(false)
  const dropdownRef = React.useRef<HTMLDivElement>(null)
  
  const isEn = pathname.startsWith('/en')
  
  React.useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false)
      }
    }
    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const switchLanguage = (lang: 'en' | 'zh') => {
    setIsOpen(false)
    if (lang === 'en' && !isEn) {
      router.push(`/en${pathname === '/' ? '' : pathname}`)
    } else if (lang === 'zh' && isEn) {
      const newPath = pathname.replace(/^\/en/, '')
      router.push(newPath === '' ? '/' : newPath)
    }
  }

  return (
    <div ref={dropdownRef} style={{ position: 'relative' }}>
      <button 
        onClick={() => setIsOpen(!isOpen)}
        style={{
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          backgroundColor: isOpen ? 'var(--surface-hover)' : 'var(--bg-color)',
          color: isOpen ? 'var(--text-primary)' : 'var(--text-secondary)',
          border: '1px solid',
          borderColor: isOpen ? 'var(--text-muted)' : 'var(--surface-border)',
          padding: '0.4rem 0.8rem',
          borderRadius: '99px',
          fontSize: '0.85rem',
          fontWeight: 500,
          cursor: 'pointer',
          transition: 'all 0.2s ease',
          boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
        }}
        onMouseEnter={(e) => {
          e.currentTarget.style.color = 'var(--text-primary)';
          e.currentTarget.style.borderColor = 'var(--text-muted)';
          e.currentTarget.style.backgroundColor = 'var(--surface-hover)';
        }}
        onMouseLeave={(e) => {
          if (!isOpen) {
            e.currentTarget.style.color = 'var(--text-secondary)';
            e.currentTarget.style.borderColor = 'var(--surface-border)';
            e.currentTarget.style.backgroundColor = 'var(--bg-color)';
          }
        }}
      >
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path><path d="M2 12h20"></path></svg>
        <span style={{ display: 'inline-block', width: '22px', textAlign: 'center' }}>
          {isEn ? 'EN' : '中'}
        </span>
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ transform: isOpen ? 'rotate(180deg)' : 'rotate(0)', transition: 'transform 0.2s' }}><polyline points="6 9 12 15 18 9"></polyline></svg>
      </button>

      {isOpen && (
        <div style={{
          position: 'absolute',
          top: 'calc(100% + 8px)',
          right: 0,
          backgroundColor: 'var(--bg-color)',
          border: '1px solid var(--surface-border)',
          borderRadius: '8px',
          padding: '4px',
          minWidth: '130px',
          display: 'flex',
          flexDirection: 'column',
          gap: '2px',
          boxShadow: '0 10px 25px -5px rgba(0,0,0,0.1)',
          animation: 'fadeIn 0.15s ease-out'
        }}>
          <button 
            onClick={() => switchLanguage('zh')}
            style={{
              textAlign: 'left',
              padding: '0.5rem 0.6rem',
              backgroundColor: !isEn ? 'var(--surface-hover)' : 'transparent',
              color: !isEn ? 'var(--text-primary)' : 'var(--text-secondary)',
              border: 'none',
              borderRadius: '4px',
              fontSize: '0.85rem',
              cursor: 'pointer',
              transition: 'background 0.2s, color 0.2s',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between'
            }}
            onMouseEnter={(e) => { if (isEn) { e.currentTarget.style.backgroundColor = 'var(--surface-hover)'; e.currentTarget.style.color = 'var(--text-primary)' } }}
            onMouseLeave={(e) => { if (isEn) { e.currentTarget.style.backgroundColor = 'transparent'; e.currentTarget.style.color = 'var(--text-secondary)' } }}
          >
            <span style={{display: 'flex', alignItems: 'center', gap: '6px'}}>🇨🇳 简体中文</span>
            {!isEn && <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>}
          </button>
          <button 
            onClick={() => switchLanguage('en')}
            style={{
              textAlign: 'left',
              padding: '0.5rem 0.6rem',
              backgroundColor: isEn ? 'var(--surface-hover)' : 'transparent',
              color: isEn ? 'var(--text-primary)' : 'var(--text-secondary)',
              border: 'none',
              borderRadius: '4px',
              fontSize: '0.85rem',
              cursor: 'pointer',
              transition: 'background 0.2s, color 0.2s',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between'
            }}
            onMouseEnter={(e) => { if (!isEn) { e.currentTarget.style.backgroundColor = 'var(--surface-hover)'; e.currentTarget.style.color = 'var(--text-primary)' } }}
            onMouseLeave={(e) => { if (!isEn) { e.currentTarget.style.backgroundColor = 'transparent'; e.currentTarget.style.color = 'var(--text-secondary)' } }}
          >
            <span style={{display: 'flex', alignItems: 'center', gap: '6px'}}>🇺🇸 English</span>
            {isEn && <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>}
          </button>
        </div>
      )}
      <style>{`
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(-4px) scale(0.96); }
          to { opacity: 1; transform: translateY(0) scale(1); }
        }
      `}</style>
    </div>
  )
}
