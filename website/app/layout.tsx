import type { Metadata } from 'next'
import './globals.css'
import LanguageDropdown from '@/components/LanguageDropdown'
import { ThemeProvider } from '@/components/ThemeProvider'
import ThemeToggle from '@/components/ThemeToggle'

export const metadata: Metadata = {
  title: 'AI Landscape 2026',
  description: '个人全栈开发者 AI 生存指南',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="zh" suppressHydrationWarning>
      <body>
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
          <div style={{ position: 'fixed', top: '1.5rem', right: '2rem', zIndex: 1000, display: 'flex', gap: '12px', alignItems: 'center' }}>
            <ThemeToggle />
            <LanguageDropdown />
          </div>
          {children}
        </ThemeProvider>
      </body>
    </html>
  )
}
