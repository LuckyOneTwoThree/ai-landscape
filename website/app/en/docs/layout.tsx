import Sidebar from '@/components/Sidebar'
import styles from '../../docs/docs-layout.module.css'

export default function EnDocsLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className={styles.container}>
      <Sidebar locale="en" />
      <main className={styles.mainContent}>
        {children}
      </main>
    </div>
  )
}
