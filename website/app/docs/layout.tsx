import Sidebar from '@/components/Sidebar'
import styles from './docs-layout.module.css'

export default function DocsLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className={styles.container}>
      <Sidebar locale="zh" />
      <main className={styles.mainContent}>
        {children}
      </main>
    </div>
  )
}
